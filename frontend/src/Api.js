import axios from "axios";

const baseUrl = import.meta.env.VITE_API_BASE_URL;
// const baseUrl = "http://localhost:8000";
const apiClient = axios.create({
	baseURL: baseUrl,
	timeout: 30000,
});

export default apiClient;
