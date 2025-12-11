import { z } from "zod";

export const SummarizedReportsScheme = z.object({
  summarized_report_id: z.coerce.number(),
  summarized_report_message: z.string(),
  work_area_id: z.coerce.number(),
  enterprise_shift_id: z.coerce.number(),
  summary_date: z.string(),
});

export const SummaryExistsScheme = z.object({
  exists: z.boolean(),
});

export type SummarizedReportsType = z.infer<typeof SummarizedReportsScheme>;
export type SummaryExistsType = z.infer<typeof SummaryExistsScheme>;
