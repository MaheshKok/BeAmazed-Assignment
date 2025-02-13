// src/App.js
import React from "react";
import { Container } from "@chakra-ui/react";
import ScriptInput from "./components/ScriptInput";

function App() {
	return (
		<Container maxW="container.lg" py={8}>
			<ScriptInput />
		</Container>
	);
}

export default App;
