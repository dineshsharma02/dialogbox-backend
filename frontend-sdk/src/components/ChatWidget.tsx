import React, { useState, useEffect, useRef } from "react";

const API_URL = "http://localhost:8080/user/query"; // to be adjusted for prod

export const ChatWidget = () => {
  type ChatMessage = {
    sender: "user" | "bot";
    text: string;
  };
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatBoxRef = useRef<HTMLDivElement>(null);

  // const tenantId = new URLSearchParams(window.location.search).get("t") || ""
  const tenantId = 1;
  const sendMessage = async () => {
    if (!input.trim()) return;
    if (loading) return;

    const userMessage: ChatMessage = { sender: "user", text: input.trim() };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);
    try {
      const res = await fetch(`${API_URL}?t=${tenantId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: input.trim() }),
      });
      const data = await res.json();
      const answer =
        data?.data?.final_answer || "Sorry, I couldn't find an answer.";
      setMessages((prev) => [...prev, { sender: "bot", text: answer }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Error fetching response." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    chatBoxRef.current?.scrollTo(0, chatBoxRef.current.scrollHeight);
  }, [messages, loading]);

  return (
    <div className="flex flex-col h-full w-full max-w-full border rounded-xl shadow-md overflow-hidden font-sans bg-white sm:rounded-2xl">

      <div className="bg-emerald-600 px-4 py-2.5 border-b shadow-sm flex items-center justify-center gap-2 text-base font-medium text-white">
        <span className="text-lg">💬</span>
        <span>DialogBox Assistant</span>
      </div>

      <div
        ref={chatBoxRef}
        className="flex-1 px-3 sm:px-4 py-4 sm:py-6 space-y-3 overflow-y-auto bg-gray-100 text-[15px] leading-relaxed tracking-normal"
      >

        {messages.map((message: ChatMessage, i: number) => (
          <div
            key={i}
            className={`w-fit max-w-[90%] sm:max-w-[75%] px-4 py-2 rounded-2xl text-[15px] leading-relaxed shadow-sm whitespace-pre-wrap ${
              message.sender === "user"
                ? "bg-emerald-600 text-white ml-auto rounded-br-none"
                : "bg-white text-gray-900 mr-auto border border-gray-300 rounded-bl-none"
            }`}
          >
            {message.text}
          </div>
        ))}
        {loading && (
   <div className="w-36 h-4 bg-gray-200 animate-pulse rounded-md mr-auto"></div>
)}

      </div>

      <div className="p-3 border-t bg-white flex gap-2 items-center">
        <input
          value={input}
          disabled={loading}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          autoFocus
          className="flex-1 text-[15px] px-4 py-2.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-50 disabled:opacity-50 transition-all"
          placeholder="Ask a question..."
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          className="px-4 py-2 bg-emerald-600 text-white rounded-md text-sm flex items-center justify-center gap-2 transition-opacity duration-150 disabled:opacity-40"
        >
          {loading ? (
            <>
              <svg
                className="animate-spin h-4 w-4 text-white"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                  fill="none"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
                />
              </svg>
              <span>Sending</span>
            </>
          ) : (
            <span>Send</span>
          )}
        </button>
      </div>
    </div>
  );
};
