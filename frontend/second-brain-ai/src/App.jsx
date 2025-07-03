import React, { useEffect, useState } from "react";
import GraphView from "./components/GraphView";
import ChatCopilot from "./components/ChatCopilot";

function App() {
  const [elements, setElements] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/build-graph", { method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        const nodes = data.nodes;
        const edges = data.edges;
        setElements([...nodes, ...edges]);
      });
  }, []);

  return (
    <div>
      <h1>Second Brain ai Co-Pilot</h1>
      <GraphView elements={elements} />
      <ChatCopilot />
    </div>
  );
}

export default App;