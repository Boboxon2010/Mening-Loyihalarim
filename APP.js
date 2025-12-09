import React, { useState } from "react";

// CSS styles - hammasi shu fayl ichida
const styles = {
  app: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    minHeight: "100vh",
    backgroundColor: "#f0f0f0",
    fontFamily: "Arial, sans-serif",
  },
  calculator: {
    background: "white",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
    width: "300px",
  },
  title: {
    textAlign: "center",
    color: "#333",
    marginBottom: "20px",
  },
  display: {
    background: "#f8f9fa",
    border: "1px solid #ddd",
    borderRadius: "5px",
    padding: "15px",
    marginBottom: "15px",
    textAlign: "right",
  },
  input: {
    fontSize: "18px",
    color: "#666",
    minHeight: "25px",
  },
  result: {
    fontSize: "24px",
    fontWeight: "bold",
    color: "#333",
    minHeight: "30px",
  },
  buttons: {
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: "10px",
  },
  button: {
    padding: "15px",
    fontSize: "18px",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    backgroundColor: "#e9ecef",
    transition: "background-color 0.2s",
  },
  operator: {
    backgroundColor: "#007bff",
    color: "white",
  },
  equals: {
    backgroundColor: "#28a745",
    color: "white",
  },
  clear: {
    backgroundColor: "#dc3545",
    color: "white",
  },
  backspace: {
    backgroundColor: "#ffc107",
    color: "black",
  },
};

export default function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const handleClick = (value) => {
    if (value === "=") {
      try {
        setResult(eval(input).toString());
      } catch (error) {
        setResult("Error");
      }
    } else if (value === "C") {
      setInput("");
      setResult("");
    } else if (value === "DEL") {
      setInput(input.slice(0, -1));
    } else {
      setInput(input + value);
    }
  };

  // Button style larini qaytaruvchi funksiya
  const getButtonStyle = (type, isZero = false) => {
    const baseStyle = { ...styles.button };

    // Grid layout sozlamalari
    const gridStyle = {};
    if (type === "equals") {
      gridStyle.gridRow = "span 2";
    }
    if (isZero) {
      gridStyle.gridColumn = "span 2";
    }

    // Button turi bo'yicha rang
    switch (type) {
      case "operator":
        return { ...baseStyle, ...styles.operator, ...gridStyle };
      case "equals":
        return { ...baseStyle, ...styles.equals, ...gridStyle };
      case "clear":
        return { ...baseStyle, ...styles.clear, ...gridStyle };
      case "backspace":
        return { ...baseStyle, ...styles.backspace, ...gridStyle };
      default:
        return { ...baseStyle, ...gridStyle };
    }
  };

  return (
    <div style={styles.app}>
      <div style={styles.calculator}>
        <h1 style={styles.title}>React Calculator</h1>

        <div style={styles.display}>
          <div style={styles.input}>{input}</div>
          <div style={styles.result}>{result}</div>
        </div>

        <div style={styles.buttons}>
          {/* 1-qator */}
          <button
            style={getButtonStyle("clear")}
            onClick={() => handleClick("C")}
          >
            C
          </button>
          <button
            style={getButtonStyle("backspace")}
            onClick={() => handleClick("DEL")}
          >
            DEL
          </button>
          <button
            style={getButtonStyle("operator")}
            onClick={() => handleClick("/")}
          >
            /
          </button>
          <button
            style={getButtonStyle("operator")}
            onClick={() => handleClick("*")}
          >
            *
          </button>

          {/* 2-qator */}
          <button style={getButtonStyle()} onClick={() => handleClick("7")}>
            7
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick("8")}>
            8
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick("9")}>
            9
          </button>
          <button
            style={getButtonStyle("operator")}
            onClick={() => handleClick("-")}
          >
            -
          </button>

          {/* 3-qator */}
          <button style={getButtonStyle()} onClick={() => handleClick("4")}>
            4
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick("5")}>
            5
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick("6")}>
            6
          </button>
          <button
            style={getButtonStyle("operator")}
            onClick={() => handleClick("+")}
          >
            +
          </button>

          {/* 4-qator */}
          <button style={getButtonStyle()} onClick={() => handleClick("1")}>
            1
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick("2")}>
            2
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick("3")}>
            3
          </button>
          <button
            style={getButtonStyle("equals")}
            onClick={() => handleClick("=")}
          >
            =
          </button>

          {/* 5-qator */}
          <button
            style={getButtonStyle("", true)}
            onClick={() => handleClick("0")}
          >
            
          </button>
          <button style={getButtonStyle()} onClick={() => handleClick(".")}>
            .
          </button>
        </div>
      </div>
    </div>
  );
}
