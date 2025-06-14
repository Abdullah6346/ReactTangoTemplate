import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New Reactango App" },
    { name: "description", content: "Welcome to Reactango!" },
  ];
}

export default function Home() {
  return <Welcome />;
}
