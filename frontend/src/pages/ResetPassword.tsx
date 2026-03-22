// src/pages/ResetPassword.tsx
import { useState } from "react";
import { useLocation } from "react-router-dom";
import { api, parseApiError } from "../lib/api";

export default function ResetPassword() {
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const location = useLocation();
  const token = new URLSearchParams(location.search).get("token");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const res = await api.post("/reset-password", {
        token,
        new_password: password,
      });

      setMessage(res.data.message);
    } catch (err) {
      setError(parseApiError(err));
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-xl font-bold mb-4">Reset Password</h1>

      <form onSubmit={handleSubmit} className="space-y-3">
        <input
          type="password"
          className="w-full border p-2"
          placeholder="New password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="w-full bg-blue-500 text-white p-2">
          Reset Password
        </button>
      </form>

      {message && <p className="text-green-600 mt-3">{message}</p>}
      {error && <p className="text-red-600 mt-3">{error}</p>}
    </div>
  );
}
