import "dotenv/config";
// @ts-ignore
import fs from "fs";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";
import { image } from "../resources/base64BufoApproval";
import { milwaukeeArtMuseumPDFBase64 } from "../resources/Milwaukee Art Museum PDF";

const client = wrapOpenAI(new OpenAI());

async function imageUrlExample() {
  const response = await client.responses.create({
    model: "gpt-4o",
    input: [
      {
        role: "user",
        content: [
          { type: "input_text", text: "what's in this image?" },
          {
            detail: "auto",
            type: "input_image",
            image_url:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        ],
      },
    ],
  });

  console.log("Image URL response:");
  console.log(response.output_text);
}

async function imageBase64Example() {
  const response = await client.responses.create({
    model: "gpt-4.1-mini",
    input: [
      {
        role: "user",
        content: [
          { type: "input_text", text: "what's in this image?" },
          {
            detail: "auto",
            type: "input_image",
            image_url: `${image}`,
          },
        ],
      },
    ],
  });

  console.log("\nImage base64 response:");
  console.log(response.output_text);
}

async function pdfUploadExample() {
  const file = await client.files.create({
    file: fs.createReadStream("./resources/Milwaukee Art Museum Summary.pdf"),
    purpose: "user_data",
  });

  const response = await client.responses.create({
    model: "gpt-4o",
    input: [
      {
        role: "user",
        content: [
          { type: "input_text", text: "what's in this pdf?" },
          {
            type: "input_file",
            file_id: file.id,
          },
        ],
      },
    ],
  });

  console.log("\nPDF upload response:");
  console.log(response.output_text);
}

async function pdfBase64Example() {
  const response = await client.responses.create({
    model: "gpt-4o",
    input: [
      {
        role: "user",
        content: [
          { type: "input_text", text: "what's in this pdf?" },
          {
            type: "input_file",
            filename: "milwaukeeArtMuseum.pdf",
            file_data: `data:application/pdf;base64,${milwaukeeArtMuseumPDFBase64}`,
          },
        ],
      },
    ],
  });

  console.log("\nPDF base64 response:");
  console.log(response.output_text);
}
async function pdfUrlExample() {
  const response = await client.responses.create({
    model: "gpt-4o",
    input: [
      {
        role: "user",
        content: [
          { type: "input_text", text: "what's in this pdf?" },
          {
            type: "input_file",
            file_url:
              "https://drive.google.com/uc?export=download&id=1m0_e3dOKrbLY3VNjnTehQ3hR-4t5V4FB",
          },
        ],
      },
    ],
  });

  console.log("Image URL response:");
  console.log(response.output_text);
}

async function multimodalExample() {
  await imageUrlExample();
  await imageBase64Example();
  await pdfUploadExample();
  await pdfBase64Example();
  await pdfUrlExample();
}

export async function main() {
  return multimodalExample();
}
