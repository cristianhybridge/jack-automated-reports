import { useSummarizedReports } from "../../hooks/useSummary";
import { Box, CloseButton, Spinner, Text, VStack } from "@chakra-ui/react";

type Props = {
  date: string;
  onClose?: () => void;
};

export function LoadSummarizedReport({ date, onClose }: Props) {
  const { data, isLoading, error } = useSummarizedReports(date);
  if (isLoading) return <Spinner />;
  if (error) return <Text color="red.500">Error loading summary</Text>;
  if (!data) return null;
  const reportDate = data.summary_date;

  return (
    <Box
      position="fixed"
      bottom=""
      right="2rem"
      w="50%"
      h="50%"
      bg="white"
      shadow="xl"
      borderRadius="md"
      p={4}
      overflowY="auto"
      zIndex={9999}
    >
      <VStack align="stretch" spacing={3}>
        <CloseButton alignSelf="flex-end" onClick={onClose} />
        {isLoading && <Spinner />}
        {error && <Text color="red.500">Error loading summary</Text>}
        {data && (
          <>
            <Text fontWeight="bold">
              Reporte turno {data.enterprise_shift_id} - Linea{" "}
              {data.work_area_id}
            </Text>
            <Text fontSize="sm">{data.summarized_report_message}</Text>
            <Text fontSize="xs" color="gray.500">
              Fecha: {reportDate}
            </Text>
          </>
        )}
      </VStack>
    </Box>
  );
}
