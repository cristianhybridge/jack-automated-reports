import CreateReport from "./Reports/CreateReport.tsx";
import { Box, Button, VStack } from "@chakra-ui/react";
import ReportsList from "./Reports/ReportsList.tsx";
import { useState } from "react";
import SummarizedReportContainer from "./Reports/SummarizedReportContainer.tsx";

function Home() {
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
            {!showResume && (
              <Button isDisabled={showResume} onClick={handleShowResume}>
                Generar resumen
              </Button>
            )}
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
