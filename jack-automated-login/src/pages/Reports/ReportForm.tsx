import {
  FormControl,
  FormLabel,
  HStack,
  Input,
  Textarea,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import {
  PostReportDetailsSchema,
  ReportDetailsType,
} from "../../schemes/ReportDetails.scheme.ts";
import { zodResolver } from "@hookform/resolvers/zod";

type Props = {};

function ReportForm({}: Props) {
  const postForm = useForm<ReportDetailsType>({
    resolver: zodResolver(PostReportDetailsSchema),
  });
  return (
    <>
      <form>
        <HStack className="mb-3">
          <FormControl id="title">
            <FormLabel htmlFor="title" className="form-FormLabel">
              Título
            </FormLabel>
            <Input type="text" id="title" className="form-control" />
          </FormControl>
          <FormControl>
            <FormLabel htmlFor="" className="form-FormLabel">
              Área
            </FormLabel>
            <Input type="text" id="work_area" className="form-control" />
          </FormControl>
        </HStack>
        <HStack className="mb-3">
          <FormControl>
            <FormLabel htmlFor="" className="form-FormLabel">
              Responsable
            </FormLabel>
            <Input type="text" id="responsible" className="form-control" />
          </FormControl>
          <FormControl>
            <FormLabel htmlFor="" className="form-FormLabel">
              Fecha
            </FormLabel>
            <Input type="text" id="created_date" className="form-control" />
          </FormControl>
        </HStack>
        <div className="mb-3">
          <FormLabel htmlFor="" className="form-FormLabel">
            Descripción
          </FormLabel>
          <Textarea id="message" className="form-control" />
        </div>
      </form>
    </>
  );
}

export default ReportForm;
