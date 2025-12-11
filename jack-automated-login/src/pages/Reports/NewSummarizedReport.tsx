import { LoadSummarizedReport } from "./LoadSummarizedReport.tsx";

type Props = {
  date: string;
};

function NewSummarizedReport({ date }: Props) {
  // const {
  //   mutate: generateSummary,
  //   isPending,
  //   data: summaryData,
  // } = useGenerateSummary(1, 1, date);

  return (
    <>
      New Summary:
      <LoadSummarizedReport date={date} />
    </>
  );
}

export default NewSummarizedReport;
