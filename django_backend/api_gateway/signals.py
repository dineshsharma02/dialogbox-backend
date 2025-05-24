from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from admin_panel.models import FAQ
from api_gateway.embedding.embedding_pipeline import embed_faqs
from api_gateway.vector.chroma_service import get_chroma_collection

@receiver(post_save, sender = FAQ)
def sync_faq_to_chroma(sender, instance, **kwargs):
   
    collection = get_chroma_collection()
    vector_id = f"{instance.tenant_id}-{instance.id}"
    print(vector_id)
    collection.delete(ids=[vector_id])

    embed_faqs(
        tenant_id=instance.tenant_id,
        faqs=[{"question":instance.question, "answer":instance.answer, "id": instance.id}],
    )

@receiver(post_delete, sender = FAQ)
def delete_faq_from_chroma(sender,instance, **kwargs):
    collection = get_chroma_collection()
    vector_id = f"{instance.tenant_id}-{instance.id}"
    print(vector_id)
    collection.delete(ids=[vector_id])