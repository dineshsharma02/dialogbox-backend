import React, {useState, useEffect, useRef} from 'react'


const API_URL = "http://127.0.0.1:8000/user/query"; // to be adjusted for prod

export const ChatWidget = () =>{
    type ChatMessage = {
        sender: "user" | "bot";
        text: string;
    };
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);
    const chatBoxRef = useRef<HTMLDivElement>(null);

    // const tenantId = new URLSearchParams(window.location.search).get("t") || ""
    const tenantId  = 2
    const sendMessage = async() =>{
        if (!input.trim()) return;

        const userMessage: ChatMessage = { sender: "user", text: input.trim() };
        setMessages((prev)=>[...prev, userMessage]);
        setInput("");
        setLoading(true);
        try{
            const res = await fetch(`${API_URL}?t=${tenantId}`,{
               
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({question: input.trim()})
            });
            const data = await res.json();
            const answer = data?.data?.final_answer || "Sorry, I couldn't find an answer.";
            setMessages((prev) => [...prev, { sender: "bot", text: answer }]);
        }
        catch(err){
            setMessages((prev) => [...prev, { sender: "bot", text: "Error fetching response." }]);
        }
        finally{
            setLoading(false);
        }

    };

    useEffect(()=>{
        chatBoxRef.current?.scrollTo(0, chatBoxRef.current.scrollHeight)
    }, [messages])

    


    return (
    <div className="flex flex-col h-full w-full border rounded-lg shadow-md overflow-hidden font-sans">
      <div className="bg-gray-800 text-white text-center py-2 text-sm">DialogBox Assistant</div>

      <div ref={chatBoxRef} className="flex-1 p-3 space-y-2 overflow-y-auto bg-gray-50">
        {messages.map((message: ChatMessage, i:number)=> (
            <div
            key={i}
            className={`max-w-[80%] px-4 py-2 rounded-lg text-sm ${
              message.sender === "user"
                ? "bg-blue-500 text-white ml-auto"
                : "bg-gray-200 text-black mr-auto"
            }`}
          >
            {message.text}
          </div>
        ))}
        {loading && (
          <div className="text-gray-500 text-xs italic animate-pulse">Assistant is typing...</div>
        )}
      </div>

      <div className="p-2 border-t flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          className="flex-1 text-sm px-3 py-2 border rounded-md focus:outline-none focus:ring"
          placeholder="Ask a question..."
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded-md text-sm disabled:opacity-50"
        >
          Send
        </button>
        
      </div>

    </div>
  );
};


