// src/pages/Register.tsx
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api } from "../api/client";

export default function Register() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    setError("");

    if (!email || !password) {
      setError("Email and password are required");
      return;
    }

    setLoading(true);
    try {
      await api.post("/auth/register", {
        email,
        password,
      });

      // optional: show feedback or toast
      navigate("/login");
    } catch (error: any) {
      setError(
        error?.response?.data?.detail ||
        JSON.stringify(error?.response?.data) ||
        "Registration failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-2xl shadow-md w-full max-w-md">
        
        <h2 className="text-2xl font-bold mb-6 text-center">
          Create account
        </h2>

        {error && (
          <div className="mb-4 text-red-600 text-sm text-center">
            {error}
          </div>
        )}

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full mb-4 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full mb-6 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className={`w-full py-2 rounded-lg text-white transition ${
            loading
              ? "bg-gray-400 cursor-not-allowed"
              : "bg-blue-600 hover:bg-blue-700"
          }`}
        >
          {loading ? "Creating..." : "Create account"}
        </button>

        {/* ✅ Back to login link */}
        <p className="mt-6 text-sm text-center text-gray-600">
          Already have an account?{" "}
          <Link
            to="/"
            className="text-blue-600 font-medium hover:underline"
          >
            Sign in
          </Link>
        </p>

      </div>
    </div>
  );
}
