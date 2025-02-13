// src/App.js
import React, { useState } from "react";
import {
	Box,
	Container,
	Heading,
	Textarea,
	Button,
	Text,
	VStack,
} from "@chakra-ui/react";
import apiClient from "./Api";

function App() {
	const [script, setScript] = useState("");
	const [intro, setIntro] = useState("");
	const [loading, setLoading] = useState(false);

	const handleGenerateIntro = async () => {
		setLoading(true);
		try {
			const response = await apiClient.post("/api/generate-intro", {
				script,
			});
			setIntro(response.data.intro);
		} catch (error) {
			console.error("Error generating intro:", error);
			setIntro("Error generating intro. Please try again.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<Container maxW="container.md" py={8}>
			<VStack spacing={6} align="stretch">
				<Heading as="h1" size="xl" textAlign="center">
					YouTube Intro Generator
				</Heading>
				<Textarea
					placeholder="Paste your video script here..."
					value={script}
					onChange={(e) => setScript(e.target.value)}
					size="lg"
					rows={10}
					resize="vertical"
				/>
				<Button
					colorScheme="blue"
					onClick={handleGenerateIntro}
					isLoading={loading}
					loadingText="Generating..."
				>
					Generate Intro
				</Button>
				{intro && (
					<Box bg="gray.50" p={6} borderRadius="md">
						<Heading as="h2" size="md" mb={4}>
							Generated Intro
						</Heading>
						<Text>{intro}</Text>
					</Box>
				)}
			</VStack>
		</Container>
	);
}

export default App;
