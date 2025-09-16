import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, value in players.items():
        nickname = player
        email = value.get("email")
        bio = value.get("bio")
        race = value.get("race")
        race_name = race.get("name")
        race_description = race.get("description", None)
        skills = race.get("skills")
        guild = value.get("guild")

        Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        race_id = Race.objects.get(name=race_name).id

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"), bonus=skill.get("bonus"),
                    race_id=race_id
                )

        if guild is not None:
            guild_name = guild.get("name")
            guild_description = guild.get("description", None)

            Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
            guild_id = Guild.objects.get(name=guild_name).id

            Player.objects.create(
                nickname=nickname, email=email, bio=bio, race_id=race_id,
                guild_id=guild_id
            )
        else:
            Player.objects.create(
                nickname=nickname, email=email,
                bio=bio, race_id=race_id, guild_id=None,
            )


if __name__ == "__main__":
    main()
