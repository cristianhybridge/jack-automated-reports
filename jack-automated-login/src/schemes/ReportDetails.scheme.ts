import { z } from "zod";

export const PostReportDetailsSchema = z.object({
  title: z.string(),
  work_area_id: z.coerce.number(),
  responsible: z.string(),
  message: z.string(),
  created_date: z.string(),
  enterprise_shift_id: z.coerce.number(),
});

export type ReportDetailsType = z.infer<typeof PostReportDetailsSchema>;
