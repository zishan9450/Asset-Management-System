"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

import { Login } from "@/components/Login";
import { api } from "@/lib/api";
import { getStoredSession, saveStoredSession } from "@/lib/session";
import { toast } from "sonner";

export default function LoginPage() {
  const router = useRouter();
  const [isAuthenticating, setIsAuthenticating] = useState(false);
  const [authError, setAuthError] = useState<string | null>(null);
  const [statusMessage, setStatusMessage] = useState<string | null>(null);

  useEffect(() => {
    const existing = getStoredSession();
    if (existing) {
      router.replace("/dashboard");
    }

    const params = new URLSearchParams(window.location.search);
    const reason = params.get("reason");
    if (reason === "expired") {
      setStatusMessage("Your session expired. Please sign in again.");
      return;
    }

    if (reason === "logout") {
      setStatusMessage("You have been logged out");
      return;
    }

    setStatusMessage(null);
  }, [router]);

  const handleLogin = async (email: string, password: string, rememberMe: boolean) => {
    setIsAuthenticating(true);
    setAuthError(null);

    try {
      const response = await api.login(email, password);
      saveStoredSession({ token: response.access_token, user: response.user }, rememberMe);
      router.replace("/dashboard");
    } catch (error) {
      const message = error instanceof Error ? error.message : "Unable to sign in";
      setAuthError(message);
      toast.error(message);
    } finally {
      setIsAuthenticating(false);
    }
  };

  return (
    <Login
      onLogin={handleLogin}
      isLoading={isAuthenticating}
      errorMessage={authError}
      statusMessage={statusMessage}
    />
  );
}
