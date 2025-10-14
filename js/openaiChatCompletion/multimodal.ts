import "dotenv/config";
// @ts-ignore
import fs from "fs";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";
import { image } from "../resources/base64BufoApproval";
import { milwaukeeArtMuseumPDFBase64 } from "../resources/Milwaukee Art Museum PDF";
const client = wrapOpenAI(new OpenAI());

async function imageUrlExample() {
  const response = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "What's in this image?",
          },
          {
            type: "image_url",
            image_url: {
              url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
          },
        ],
      },
    ],
  });

  console.log("Image URL response:");
  console.log(response.choices[0].message.content);
}

async function imageBase64Example() {
  const response = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Describe this image in detail.",
          },
          {
            type: "image_url",
            image_url: {
              url: image,
            },
          },
        ],
      },
    ],
  });

  console.log("\nImage base64 response:");
  console.log(response.choices[0].message.content);
}

async function pdfUploadExample() {
  const file = await client.files.create({
    file: fs.createReadStream("./resources/Milwaukee Art Museum Summary.pdf"),
    purpose: "user_data",
  });
  const response = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Please summarize this PDF document.",
          },
          {
            type: "file",
            file: {
              file_id: file.id,
            },
          },
        ],
      },
    ],
  });

  console.log("\nPDF response:");
  console.log(response.choices[0].message.content);
}

async function pdfExampleBase64() {
  const response = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Please summarize this PDF document.",
          },
          {
            type: "file",
            file: {
              filename: "milwaukeeArtMuseum.pdf",
              file_data: `data:application/pdf;base64,${milwaukeeArtMuseumPDFBase64}`,
            },
          },
        ],
      },
    ],
  });

  console.log("\nPDF response:");
  console.log(response.choices[0].message.content);
}

async function audioInputExample() {
  // Fetch an audio file and convert it to a base64 string
  const url = "https://cdn.openai.com/API/docs/audio/alloy.wav";
  const audioResponse = await fetch(url);
  const buffer = await audioResponse.arrayBuffer();

  // Convert ArrayBuffer to base64
  const bytes = new Uint8Array(buffer);
  let binary = "";
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  const base64str = btoa(binary);

  const response = await client.chat.completions.create({
    model: "gpt-4o-audio-preview",
    modalities: ["text", "audio"],
    audio: { voice: "alloy", format: "wav" },
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: "What is in this recording?" },
          {
            type: "input_audio",
            input_audio: { data: base64str, format: "wav" },
          },
        ],
      },
    ],
    store: true,
  });

  console.log(response.choices[0]);
}

async function audioOutputExample() {
  const response = await client.chat.completions.create({
    model: "gpt-4o-audio-preview",
    modalities: ["text", "audio"],
    audio: { voice: "alloy", format: "wav" },
    messages: [{ role: "user", content: "Hello! Tell me a short joke." }],
  });

  console.log("\nAudio output response:");
  console.log("Text:", response.choices[0].message.content);
  console.log("Audio data available:", !!response.choices[0].message.audio);
}

export async function main() {
  await imageUrlExample();
  await imageBase64Example();
  await pdfUploadExample();
  await pdfExampleBase64();
  await audioInputExample();
  await audioOutputExample();
}
