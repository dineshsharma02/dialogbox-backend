from django.shortcuts import render

from .forms import FAQUploadForm
import csv
import io
from api_gateway.embedding.embedding_pipeline import embed_faqs
from .models import FAQ
import uuid

def upload_faq_view(request):
    if request.method=="POST":
        form = FAQUploadForm(request.POST, request.FILES)
        if form.is_valid():
            tenant_id = form.cleaned_data["tenant_id"]
            file = request.FILES["csv_file"]
            decoded_file = file.read().decode("utf-8")
            reader = csv.DictReader(io.StringIO(decoded_file))
            try:
                faq_objs = []

                for row in reader:
                    question = row["question"].strip()
                    answer = row.get("answer", "").strip()
                    faq = FAQ(tenant_id=tenant_id, question=question, answer=answer)
                    faq.save() 
                    faq_objs.append(faq)
                
                faqs_for_embedding = [
                    {"id": str(faq.id), "question": faq.question, "answer": faq.answer}
                    for faq in faq_objs
                ]

                # Embed using pre-generated IDs
                embed_faqs(int(tenant_id), faqs_for_embedding)


                return render(request, "upload_success.html", {"tenant_id": tenant_id, "count": len(faqs_for_embedding)})
            except Exception as e:
                return render(request, "error.html", {"error": str(e)})
    else:
        form = FAQUploadForm()

        return render(request, "upload_faq.html", {"form": form})