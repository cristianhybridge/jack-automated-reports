import { Outlet } from "react-router-dom";
import { Flex, HStack, Stack } from "@chakra-ui/react";
import { getToday } from "../utils/GetTodayDate.ts";

export default function MainLayout() {
  const todayDate = getToday().toDateString();
  return (
    <>
      <header
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          right: 0,
          height: "60px",
          background: "#222",
          color: "white",
          display: "flex",
          alignItems: "center",
          padding: "0 1rem",
          zIndex: 1000,
          fontFamily: "monospace",
        }}
      >
        <Flex>
          <Stack>
            <h2>Jack Assistant</h2>
            <h2>{todayDate}</h2>
          </Stack>
        </Flex>
      </header>

      {/* Page container pushed down by header */}
      <main style={{ paddingTop: "60px" }}>
        <Outlet />
      </main>
    </>
  );
}
