from langflow import CustomComponent
from langchain.schema import Document

class FlowRunner(CustomComponent):
    display_name = "Flow Runner"
    description = "Run other flows using a document as input."

    def build_config(self):
        flows = self.list_flows()
        flow_names = [f.name for f in flows]
        return {"flow_name": {"options": flow_names,
                              "display_name": "Flow Name",
                              },
                "document": {"display_name": "Document"}
                }


    def build(self, flow_name: str, document: Document) -> Document:
        # List the flows
        flows = self.list_flows()
        # Get the flow that matches the selected name
        # You can also get the flow by id
        # using self.get_flow(flow_id=flow_id)
        tweaks = {}
        flow = self.get_flow(flow_name=flow_name, tweaks=tweaks)
        # Get the page_content from the document
        if document and isinstance(document, list):
            document = document[0]
        page_content = document.page_content
        # Use it in the flow
        result = flow(page_content)
        return Document(page_content=str(result))
