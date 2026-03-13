import type { Metadata } from "next";
import { AppToaster } from "@/components/ui/toaster";
import "./globals.css";

export const metadata: Metadata = {
  title: "Asset Management System",
  description: "Enterprise asset management application",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
        <AppToaster />
      </body>
    </html>
  );
}
