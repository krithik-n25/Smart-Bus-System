from app.core.config import supabase_admin
from typing import Optional

async def log_audit(
    user_id: Optional[str],
    action: str,
    entity_type: str,
    entity_id: Optional[str],
    old_value: Optional[dict],
    new_value: Optional[dict],
    ip_address: Optional[str] = None
):
    """
    Log every important action permanently.
    Never raises exceptions — audit logging
    should never break your main flow.
    """
    try:
        supabase_admin.table("audit_logs").insert({
            "user_id": user_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "old_value": old_value,
            "new_value": new_value,
            "ip_address": ip_address
        }).execute()
    except Exception as e:
        print(f"Audit log failed: {e}")