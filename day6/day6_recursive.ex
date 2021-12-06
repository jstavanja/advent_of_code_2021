defmodule FishReproduction do

    def process_day_until_nonzero(fish_list, days_left) do
        IO.inspect(days_left)
        if (days_left > 0) do
            process_day_until_nonzero(process_day(fish_list), days_left - 1)
        else
            fish_list
        end
    end

    def process_day(fish_list) do
        List.foldl(fish_list, [], fn(current_fish, acc) -> process_fish(current_fish, acc) end)
    end

    def process_fish(fish, acc) do
      case fish do
          0 ->
              acc ++ [6, 8]
          _ ->
              acc ++ [fish-1]
      end
    end

    def run_simulation(initial_fish_list, days) do
        process_day_until_nonzero(initial_fish_list, days)
    end
end

{:ok, file_contents} = File.read("../inputs/day6/1.txt")

trimmed_fish_state_string = file_contents |> String.trim("\n")

fish_list = trimmed_fish_state_string
    |> String.split(",", trim: true)
    |> Enum.map(&String.to_integer/1)

end_fish_state = FishReproduction.run_simulation(fish_list, 80)

IO.inspect length(end_fish_state)
