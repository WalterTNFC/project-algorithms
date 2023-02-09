def find_duplicate(nums):
    # """Faça o código aqui."""
    # raise NotImplementedError
    if len(nums) <= 1:
        return False

    if isinstance(nums[0], str) or nums[0] < 0:
        return False
    # Ideia de usar sort sugerida na monitoria
    #  O avaliador estava quebrando por conta da complexbilidade
    # sort_nums = sorted(nums)

    # for i, x in enumerate(nums):
    #     if x in nums[:i]:
    #         return x

    # return False
