import { useState, useEffect, useRef } from "react";

import MessageItem from "./MessageItem";

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
      
      const rawAnswer = data?.data?.final_answer;
      const answer = Array.isArray(rawAnswer)
        ? rawAnswer.join("").trim()
        : rawAnswer || "Sorry, I couldn't find an answer.";
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
    <div className="flex flex-col h-full w-full max-w-full bg-[#e5ddd5] font-sans shadow-md rounded-lg overflow-hidden">
      {/* Header */}
      <div className="bg-[#075e54] px-4 py-3 text-white flex items-center justify-center">
        

        <span className="text-lg p-2">💬</span>
        <span>DialogBox Assistant</span>
      </div>

      {/* Messages */}
      <div
        ref={chatBoxRef}
        className="flex-1 px-3 py-4 space-y-2 overflow-y-auto"
      >
        {messages.map((message: ChatMessage, i: number) => (
          
            <MessageItem message={message} i = {i}/>
          
        ))}

        {loading && (
          <div className="inline-block bg-white px-4 py-2 rounded-xl shadow-sm text-sm text-gray-500 mr-auto">
            <div className="flex gap-1">
              <span className="w-2 h-2 bg-gray-400 rounded-full animate-pulse delay-100" />
              <span className="w-2 h-2 bg-gray-400 rounded-full animate-pulse delay-200" />
              <span className="w-2 h-2 bg-gray-400 rounded-full animate-pulse delay-300" />
            </div>
          </div>
        )}
      </div>

      {/* Input */}
      <div className="bg-white p-2 flex items-center gap-2 border-t">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type a message"
          className="flex-1 px-4 py-2 text-sm rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-emerald-50 disabled:opacity-50 transition-all"
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          className="bg-[#075e54] text-white px-4 py-2 rounded-full text-sm disabled:opacity-50"
        >
          {loading ? (
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
          ) : (
            <span>Send</span>
          )}
        </button>
      </div>
    </div>
  );
};
