from typing import Optional
from pydantic import BaseModel, Field
from .base_response import BaseResponse


class AppDefinitionResponse(BaseResponse):
    app_id: str = Field(None, description="App ID")


class AppCreationResponse(BaseResponse):
    app_id: str = Field(None, description="Generated app ID")
    app_name: Optional[str] = Field(None, description="Name of created app")
    sections_created: Optional[int] = Field(
        None, description="Number of sections created"
    )


class FieldOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where field was modified")
    field_name: Optional[str] = Field(None, description="Name of the field")


class PageBreakOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where page break was modified")
    page_index: Optional[int] = Field(None, description="Page index")


class SectionOperationResponse(BaseResponse):
    app_id: str = Field(description="App ID where section was modified")
    source_section_index: Optional[int] = Field(None, description="Source section index")
    target_section_index: Optional[int] = Field(None, description="Target section index")
    source_page_index: Optional[int] = Field(None, description="Source page index")
    target_page_index: Optional[int] = Field(None, description="Target page index")


class AddSectionResponse(BaseResponse):
    app_id: str = Field(description="App ID where section was added")
    section_id: Optional[str] = Field(None, description="Generated section ID")
    section_index: Optional[int] = Field(None, description="Index where section was added")
    section_name: Optional[str] = Field(None, description="Name of the added section")


class UpdateSectionResponse(BaseResponse):
    app_id: str = Field(description="App ID where section was updated")
    section_index: Optional[int] = Field(None, description="Index of the updated section")
    section_name: Optional[str] = Field(None, description="Name of the updated section")
