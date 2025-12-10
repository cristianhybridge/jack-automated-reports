import { z } from "zod";

export const GetReportDetailsSchema = z.object({
  report_details_id: z.coerce.number(),
  title: z.string(),
  work_area_id: z.coerce.number(),
  responsible_id: z.coerce.number(),
  message: z.string(),
  created_at: z.string(),
  enterprise_shift_id: z.coerce.number(),
  loss_time_count: z.coerce.number(),
})

export const PostReportDetailsSchema = z.object({
  title: z.string(),
  work_area_id: z.coerce.number(),
  responsible_id: z.coerce.number(),
  message: z.string(),
  created_at: z.string(),
  enterprise_shift_id: z.coerce.number(),
  loss_time_count: z.coerce.number(),

});

export type PostReportDetailsType = z.infer<typeof PostReportDetailsSchema>;
export type GetReportDetailsType = z.infer<typeof GetReportDetailsSchema>;
