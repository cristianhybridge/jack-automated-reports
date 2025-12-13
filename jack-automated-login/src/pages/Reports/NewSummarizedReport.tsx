import { LoadSummarizedReport } from "./LoadSummarizedReport.tsx";
import { useGenerateSummary } from "../../hooks/useSummary.ts";
import { Spinner } from "@chakra-ui/react";
import { useEffect } from "react";

type Props = {
  date: string;
};

function NewSummarizedReport({ date }: Props) {
  const { mutate, isPending, isSuccess } = useGenerateSummary(1, 1, date);

  useEffect(() => {
    mutate();
  }, []); // empty dependency array ensures it runs exactly once

  // show spinner while pending
  if (isPending)
    return (
      <div className="flex items-center gap-2">
        <Spinner size="sm" />
        Generando reporte con IA. Por favor espera...
      </div>
    );

  // after success, render the loaded summary
  if (isSuccess) return <LoadSummarizedReport date={date} />;

  return null; // fallback (should not happen)
}

export default NewSummarizedReport;
