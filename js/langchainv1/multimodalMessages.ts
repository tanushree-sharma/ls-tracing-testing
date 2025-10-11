import { HumanMessage } from "langchain";
import { image } from "../resources/base64BufoApproval";
import { milwaukeeArtMuseumPDFBase64 } from "../resources/Milwaukee Art Museum PDF";

export function getImageUrlMessage() {
  return new HumanMessage({
    content: [
      {
        type: "text",
        text: "Describe this image:",
      },
      {
        type: "image_url",
        image_url: {
          url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        },
      },
    ],
  });
}

export function getImageBase64Message() {
  return new HumanMessage({
    content: [
      {
        type: "text",
        text: "Describe this image, then generate an intense version of it",
      },
      {
        type: "image_url",
        image_url: {
          url: image,
        },
      },
    ],
  });
}

export function getGenerateImageMessage() {
  return new HumanMessage({
    content: [
      {
        type: "text",
        text: "Generate an image of a cartoon cat and return it as multimodal png block",
      },
    ],
  });
}

export function getPDFInputMessage() {
  return new HumanMessage({
    content: [
      {
        type: "text",
        text: "Please summarize this PDF document:",
      },
      {
        type: "file",
        data: milwaukeeArtMuseumPDFBase64,
        mimeType: "application/pdf",
      },
    ],
  });
}
