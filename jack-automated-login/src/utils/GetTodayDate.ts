export function getToday() {
  return new Date();
}

export function getYesterday() {
  const d = new Date();
  d.setDate(d.getDate() - 1);
  return d;
}

export function getPreYesterday() {
  const d = new Date();
  d.setDate(d.getDate() - 2);
  return d;
}

export function getNowFormatted() {
  return new Date().toLocaleString("en-US", {
    timeZone: "America/Tijuana", // or "America/Tijuana"
    year: "numeric",
    month: "short",
    day: "2-digit",
    // hour: "2-digit",
    // minute: "2-digit",
    // second: "2-digit",
    hour12: true,
  });
}

export function buildTimelineDates() {
  return {
    initDate: getYesterday(),
    endDate: getToday(),
  };
}
