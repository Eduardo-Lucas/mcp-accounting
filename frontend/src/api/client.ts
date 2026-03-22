// src/api/client.ts
import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8000",
  withCredentials: false, // important (avoid CORS preflight issues)
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
