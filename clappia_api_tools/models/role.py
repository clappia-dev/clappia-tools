from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from enum import Enum


class RoleType(str, Enum):
    """Role type enumeration"""
    GLOBAL = "global"
    CUSTOM = "custom"

class Role(BaseModel):
    """Role model for user permissions"""
    role_id: Optional[str] = Field(None, description="Role ID")
    role_name: str = Field(default="Custom", description="Role name")
    role_desc: str = Field(default="", description="Role description")
    role_type: RoleType = Field(default=RoleType.CUSTOM, description="Role type")
    
    can_edit_app: bool = Field(default=False, description="Can edit app")
    can_edit_data: bool = Field(default=False, description="Can edit data")
    can_view_data: bool = Field(default=False, description="Can view data")
    can_change_status: bool = Field(default=False, description="Can change status")
    can_submit_data: bool = Field(default=False, description="Can submit data")
    can_view_analytics: bool = Field(default=False, description="Can view analytics")
    can_bulk_upload: bool = Field(default=False, description="Can bulk upload")
    can_delete_data: bool = Field(default=False, description="Can delete data")
    
    def assign_from_json(self, json_data: Dict[str, Any]):
        """Assign role data from JSON"""
        self.role_id = json_data.get('roleId')
        self.role_name = json_data.get('roleName', 'Custom')
        self.role_desc = json_data.get('roleDesc', '')
        self.role_type = RoleType(json_data.get('roleType', 'custom'))
        
        self.can_edit_app = json_data.get('canEditApp') is True
        self.can_edit_data = json_data.get('canEditData') is True
        self.can_view_data = json_data.get('canViewData') is True
        self.can_change_status = json_data.get('canChangeStatus') is True
        self.can_submit_data = json_data.get('canSubmitData') is True
        self.can_view_analytics = json_data.get('canViewAnalytics') is True
        self.can_delete_data = json_data.get('canDeleteData') is True
        
        can_bulk_upload_v2 = json_data.get('canBulkUploadV2')
        if can_bulk_upload_v2 is True:
            self.can_bulk_upload = True
        elif can_bulk_upload_v2 is None and self.can_submit_data:
            # For users assigned apps before Apr-2021, canBulkUploadV2 used to be empty. So deciding using canSubmitData
            self.can_bulk_upload = True
        else:
            self.can_bulk_upload = False