import React from "react";
import CytoscapeComponent from "react-cytoscapejs";

const GraphView = ({ elements }) => {
  return (
    <CytoscapeComponent
      elements={elements}
      style={{ width: "100%", height: "600px" }}
      layout={{ name: "cose" }}
    />
  );
};

export default GraphView;