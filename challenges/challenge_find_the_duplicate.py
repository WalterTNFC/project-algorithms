def find_duplicate(nums):
    # """Faça o código aqui."""
    # raise NotImplementedError
    if len(nums) <= 1:
        return False

    if isinstance(nums[0], str) or nums[0] < 0:
        return False

    # Ideia de ordenar sugerida na monitoria
    #  O avaliador estava quebrando por conta da complexbilidade
    sort_nums = sorted(nums)

    for i, num in enumerate(sort_nums[:-1]):
        if num == sort_nums[i + 1]:
            return num

    return False
