import { Box, Button, Container, Flex, VStack } from "@chakra-ui/react";
import ReportForm from "./ReportForm.tsx";

type Props = {};

function CreateReport({}: Props) {
  return (
    <Box maxW="lg" mt={8}>
      <VStack spacing={2} align="stretch">
        <ReportForm />

        <Flex justify="flex-end">
          <Button colorScheme="blue">Agregar</Button>
        </Flex>
      </VStack>
    </Box>
  );
}

export default CreateReport;
