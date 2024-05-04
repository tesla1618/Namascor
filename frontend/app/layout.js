import { Ubuntu } from "next/font/google";
import "./globals.css";
import Sidebar from "./layout/sidebar/Sidebar";

const ubuntu = Ubuntu({
  subsets: ["latin"],
  weight: ["400"],
  display: "swap",
});

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={ubuntu.className}>
        <Sidebar children={children} />
      </body>
    </html>
  );
}
