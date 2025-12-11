import CreateReport from "./Reports/CreateReport.tsx";
import { Box, Button, Divider, HStack, VStack } from "@chakra-ui/react";
import ReportsList from "./Reports/ReportsList.tsx";
import { useState } from "react";
import SummarizedReportContainer from "./Reports/SummarizedReportContainer.tsx";
import { useSummaryExists } from "../hooks/useSummary.ts";

type Props = {};

function Home({}: Props) {
  const [showResume, setShowResume] = useState<boolean>(false);
  const handleShowResume = () => {
    if (!showResume) setShowResume(true);
  };
  return (
    <>
      <Box ms={8}>
        <VStack
          position="fixed"
          top="55"
          left="0"
          w="500px"
          bg="white"
          spacing={4}
          p={4}
        >
          <CreateReport />
          <Box w="100%" textAlign="right">
            <Button isDisabled={showResume} onClick={handleShowResume}>
              {!showResume ? "Generar resumen" : "Resumen Generado"}
            </Button>
          </Box>
          {showResume && <SummarizedReportContainer date="2025-05-12" />}
        </VStack>

        <Box ml="500px" p={4}>
          <ReportsList />
        </Box>
      </Box>
    </>
  );
}

export default Home;
