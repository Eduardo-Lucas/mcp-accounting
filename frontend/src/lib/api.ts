// src/lib/api.ts
import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8000", // adjust if needed
});

export const parseApiError = (error: any): string => {
  return (
    error?.response?.data?.detail ||
    error?.response?.data?.message ||
    "Unexpected error"
  );
};
