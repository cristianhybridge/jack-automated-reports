import { useSummaryExists } from "../../hooks/useSummary.ts";
import NewSummarizedReport from "./NewSummarizedReport.tsx";
import { LoadSummarizedReport } from "./LoadSummarizedReport.tsx";
import { useState } from "react";

type Props = {
  date: string;
};

function SummarizedReportContainer({ date }: Props) {
  const { isError: emptySummary } = useSummaryExists(date);
  const [closedWindow, setClosedWindow] = useState(false);
  const handleCloseWindow = () => setClosedWindow(true);

  if (emptySummary) return <NewSummarizedReport date={date} />;
  if (closedWindow) return null;
  if (!emptySummary)
    return (
      <>
        Resumen disponible
        <LoadSummarizedReport date={date} onClose={handleCloseWindow} />
      </>
    );
}

export default SummarizedReportContainer;
