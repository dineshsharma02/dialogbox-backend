from django.shortcuts import render

from .forms import FAQUploadForm
import csv
import io
from api_gateway.embedding.embedding_pipeline import embed_faqs
from .models import FAQ

def upload_faq_view(request):
    if request.method=="POST":
        form = FAQUploadForm(request.POST, request.FILES)
        if form.is_valid():
            tenant_id = form.cleaned_data["tenant_id"]
            file = request.FILES["csv_file"]
            decoded_file = file.read().decode("utf-8")
            reader = csv.DictReader(io.StringIO(decoded_file))
            try:
                faqs = []
                for row in reader:
                    question = row["question"].strip()
                    answer = row.get("answer", "").strip()
                    FAQ.objects.create(question=question, answer=answer, tenant_id=tenant_id)
                    faqs.append({"question": question, "answer": answer})  # changed from just question

                embed_faqs(int(tenant_id), faqs)
                return render(request, "upload_success.html", {"tenant_id": tenant_id, "count": len(faqs)})
            except:
                return render("Some Error Occured")
    else:
        form = FAQUploadForm()

        return render(request, "upload_faq.html", {"form": form})