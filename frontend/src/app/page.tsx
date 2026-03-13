"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

import { getStoredSession } from "@/lib/session";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    const session = getStoredSession();
    router.replace(session ? "/dashboard" : "/login");
  }, [router]);

  return <div className="flex min-h-screen items-center justify-center bg-gray-50 text-gray-600">Loading application...</div>;
}
