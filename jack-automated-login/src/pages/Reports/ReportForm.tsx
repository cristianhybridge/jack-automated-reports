import {
  Box,
  Button,
  FormControl,
  FormLabel,
  HStack,
  Input,
  Textarea,
  VStack,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  PostReportDetailsSchema,
  PostReportDetailsType,
} from "../../schemes/ReportDetails.scheme.ts";
import { getToday } from "../../utils/GetTodayDate.ts";
import { useCreateReports } from "../../hooks/useReportDetails.ts";

type Props = {
  onSuccess?: () => void;
};

function ReportForm({ onSuccess }: Props) {
  const todayDate = getToday().toDateString();
  const form = useForm<PostReportDetailsType>({
    resolver: zodResolver(PostReportDetailsSchema),
    defaultValues: {
      title: "",
      work_area_id: 0,
      responsible_id: 0,
      created_at: todayDate,
      enterprise_shift_id: 0,
      message: "",
      loss_time_count: 0,
    },
  });

  const { mutate } = useCreateReports();

  const submitForm = (data: PostReportDetailsType) => {
    mutate(data, {
      onSuccess: () => {
        form.reset();
        if (onSuccess) onSuccess();
      },
    });
  };

  return (
    <form onSubmit={form.handleSubmit(submitForm)}>
      <VStack spacing={5} w="100%">
        <HStack w="100%" spacing={4}>
          <FormControl id="title">
            <FormLabel>Título</FormLabel>
            <Input type="text" {...form.register("title")} />
          </FormControl>

          <FormControl id="work_area_id">
            <FormLabel>Área</FormLabel>
            <Input type="number" {...form.register("work_area_id")} />
          </FormControl>
        </HStack>

        <HStack w="100%" spacing={4}>
          <FormControl id="responsible_id">
            <FormLabel>No. Empleado</FormLabel>
            <Input type="number" {...form.register("responsible_id")} />
          </FormControl>

          <FormControl id="created_at">
            <FormLabel>Fecha</FormLabel>
            <Input type="date" {...form.register("created_at")} />
          </FormControl>
        </HStack>

        <HStack><FormControl id="enterprise_shift_id">
          <FormLabel>Turno</FormLabel>
          <Input type="number" {...form.register("enterprise_shift_id")} />
        </FormControl>
          <FormControl id="enterprise_shift_id">
            <FormLabel>Tiempo muerto</FormLabel>
            <Input type="number" {...form.register("loss_time_count")} />
          </FormControl></HStack>

        <FormControl id="message">
          <FormLabel>Descripción</FormLabel>
          <Textarea {...form.register("message")} placeholder="Detalles..." />
        </FormControl>

        <Box w="100%" textAlign="right">
          <Button
            colorScheme="purple"
            type="submit"
            // isLoading={isLoading} // disable + show spinner while posting
          >
            Enviar reporte
          </Button>
        </Box>
      </VStack>
    </form>
  );
}

export default ReportForm;
