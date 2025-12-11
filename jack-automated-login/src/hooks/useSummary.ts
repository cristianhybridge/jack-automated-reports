import {
  useMutation,
  UseMutationResult,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import {
  SummarizedReportsType,
  SummaryExistsType,
} from "../schemes/SummarizedReports.scheme.ts";
import axios from "axios";

export function useSummaryExists(date: string) {
  const getApiUrl = `http://127.0.0.1:5000/api/summarized-reports/exists/${date}`;
  return useQuery<SummaryExistsType, Error>({
    queryKey: ["summary_exists"],
    staleTime: 0,
    queryFn: () =>
      axios.get<SummaryExistsType>(getApiUrl).then((res) => res.data),
  });
}

export function useSummarizedReports(date: string) {
  const apiUrl = `http://127.0.0.1:5000/api/summarized-reports/filtered/${date}`;
  return useQuery<SummarizedReportsType, Error>({
    queryKey: ["summarized_reports"],
    staleTime: 0,
    queryFn: () =>
      axios.get<SummarizedReportsType>(apiUrl).then((res) => res.data),
  });
}

export function useGenerateSummary(
  workAreaId: number,
  enterpriseShiftId: number,
  summaryDate: string,
): UseMutationResult {
  const apiUrl = `
  http://127.0.0.1:5000/api/summarized-reports/generate-summary/${workAreaId}/${enterpriseShiftId}/${summaryDate}`;
  return useMutation({
    mutationFn: () => axios.post(apiUrl).then((res) => res.data),
  });
}
