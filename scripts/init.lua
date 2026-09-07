-- Build: 4095c46d6f27c2982e3ddf66b2299da4
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
