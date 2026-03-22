// src/pages/VerifyEmail.tsx
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { api } from "../lib/api";

export default function VerifyEmail() {
  const [status, setStatus] = useState("loading");
  const location = useLocation();

  useEffect(() => {
    const token = new URLSearchParams(location.search).get("token");

    if (!token) {
      setStatus("error");
      return;
    }

    api.get(`/verify-email?token=${token}`)
      .then(() => setStatus("success"))
      .catch(() => setStatus("error"));
  }, [location]);

  return (
    <div className="text-center mt-10">
      {status === "loading" && <p>Verifying...</p>}
      {status === "success" && <p className="text-green-600">Email verified ✅</p>}
      {status === "error" && <p className="text-red-600">Invalid or expired link</p>}
    </div>
  );
}
