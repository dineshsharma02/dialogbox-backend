import React from "react";
import ReactMarkDown from "react-markdown";

function formatMessage(text: string) {
  // Convert all single \n to markdown line breaks (two spaces + \n)
  // This will make react-markdown render each \n as a <br/>
  return text.replace(/\\n/g, "\n");
}


type MessageItemProps = { message: ChatMessage; i: number };

type ChatMessage = {
    sender: "user" | "bot";
    text: string;
  };

const cleanMessage = (text?: string) => {
  if (!text) return "";
  return text.replace(/^["“”']+|["“”']+$/g, "").trim();
};

const MessageItem = ({message, i}:MessageItemProps) => {
  return (
    <div className={`flex w-full mb-2 ${message.sender === "user" ? "justify-end" : "justify-start"}`}>
        {/* Bubble */}
        <div
            className={`px-4 py-2 text-[15px] leading-relaxed whitespace-pre-wrap rounded-xl shadow-sm ${
            message.sender === "user"
                ? "bg-[#dcf8c6] text-black rounded-br-none"
                : "bg-white text-gray-900 rounded-bl-none"
            }`}
            style={{ maxWidth: "80%" }}
        >
            <ReactMarkDown children={formatMessage(cleanMessage(message.text))} />
        </div>
    </div>
  );
};

export default MessageItem;
