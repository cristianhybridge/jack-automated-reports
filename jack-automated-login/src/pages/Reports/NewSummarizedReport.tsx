import { LoadSummarizedReport } from "./LoadSummarizedReport.tsx";
import { useGenerateSummary } from "../../hooks/useSummary.ts";
import { Spinner } from "@chakra-ui/react";
import { useEffect, useRef } from "react";

type Props = {
  date: string;
};

function NewSummarizedReport({ date }: Props) {
  const { mutate, isPending, isSuccess } = useGenerateSummary(1, 1, date);
  const hasTriggered = useRef(false);

  // Segun la IA, para no cancelar el Strict Mode y no gastarme un feriezon
  // probando la API en modo dev, esto me servira, sin embargo,
  // En produccion la doble inicializacion no sucederia...
  useEffect(() => {
    if (hasTriggered.current) return;

    hasTriggered.current = true;
    mutate();
  }, [mutate]);

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

  return null;
}

export default NewSummarizedReport;
