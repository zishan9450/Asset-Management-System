"use client";

import Image from "next/image";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Checkbox } from "@/components/ui/checkbox";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

interface LoginProps {
  onLogin: (email: string, password: string, rememberMe: boolean) => Promise<void>;
  isLoading: boolean;
  errorMessage: string | null;
  statusMessage: string | null;
}

export function Login({ onLogin, isLoading, errorMessage, statusMessage }: LoginProps) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (email && password) {
      await onLogin(email, password, rememberMe);
    }
  };

  return (
    <div
      className="relative flex min-h-screen items-center justify-center"
      style={{
        backgroundImage: "url('/login-bg.png')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
      }}
    >
      <div className="absolute inset-0 bg-black/40" />
      <div className="relative z-10 w-full max-w-md p-6">
        <Card className="bg-white/95 shadow-xl backdrop-blur-sm">
          <CardHeader className="space-y-4 text-center">
            <div className="flex justify-center">
              <Image src="/ams-logo.png" alt="AMS Logo" width={80} height={80} className="h-20 w-20 object-contain" />
            </div>
            <CardTitle className="text-2xl font-medium text-gray-900">
              Asset Management System
            </CardTitle>
            <CardDescription className="text-gray-600">
              Please sign-in to your account
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              {errorMessage ? (
                <div className="rounded-md border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
                  {errorMessage}
                </div>
              ) : null}

              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="password">Password</Label>
                <Input
                  id="password"
                  type="password"
                  placeholder="Enter your password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>

              <div className="flex items-center gap-2">
                <Checkbox id="remember" checked={rememberMe} onCheckedChange={setRememberMe} />
                <Label htmlFor="remember" className="text-sm text-gray-600">
                  Remember me
                </Label>
              </div>

              <Button type="submit" className="w-full">
                {isLoading ? "SIGNING IN..." : "LOGIN"}
              </Button>
            </form>
          </CardContent>
        </Card>

        {statusMessage ? (
          <div className="mt-4 flex items-center justify-center gap-2 rounded-md bg-green-600 px-4 py-3 text-center text-white shadow-lg">
            <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <span>{statusMessage}</span>
          </div>
        ) : null}
      </div>
    </div>
  );
}
