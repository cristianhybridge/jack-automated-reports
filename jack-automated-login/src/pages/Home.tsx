import CreateReport from "./Reports/CreateReport.tsx";
import { Box, Button, HStack } from "@chakra-ui/react";
import ReportsList from "./Reports/ReportsList.tsx";
import { getToday } from "../utils/GetTodayDate.ts";
import { useState } from "react";

type Props = {};

function Home({}: Props) {
  const todayDate = getToday().toDateString();
  const [showResume, setShowResume] = useState<boolean>(false);
  const handleShowResume = () => {
    if (!showResume) setShowResume(true);
  };
  return (
    <>
      <Box m={5}>
        <HStack>
          <CreateReport />
          <ReportsList />
        </HStack>
        <Button isDisabled={showResume} onClick={handleShowResume} mt={5}>
          {!showResume ? <>Generar resumen</> : <>Resumen Generado</>}
        </Button>
        {showResume && <>Resumen...</>}
      </Box>
    </>
  );
}

export default Home;
