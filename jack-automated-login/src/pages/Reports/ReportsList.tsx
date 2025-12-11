import { useReportDetails } from "../../hooks/useReportDetails.ts";
import { List } from "@chakra-ui/react";
import ReportItem from "./ReportItem.tsx";

function ReportsList() {
  const { data: reportsData = [], isLoading: reportsDataLoading } =
    useReportDetails();

  return (
    <List spacing={3}>
      {reportsData.map((r) => (
        <ReportItem report={r} key={r.report_details_id} />
      ))}
    </List>
  );
}

export default ReportsList;
