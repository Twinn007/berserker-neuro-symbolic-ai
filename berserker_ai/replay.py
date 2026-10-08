from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class BattleTelemetryRecord:
    turn_index: int
    enemy_distance: float
    enemy_health_pct: float
    berserker_health_pct: float
    barrier_active: bool
    action_taken: str
    symbolic_state: str
    reward: float
    outcome: str


class ReplayLogger:
    def __init__(self):
        self.records: List[BattleTelemetryRecord] = []

    def log_turn(
        self,
        turn_index: int,
        enemy_distance: float,
        enemy_health_pct: float,
        berserker_health_pct: float,
        barrier_active: bool,
        action_taken: str,
        symbolic_state: str,
        reward: float,
        outcome: str,
    ) -> None:
        record = BattleTelemetryRecord(
            turn_index=turn_index,
            enemy_distance=enemy_distance,
            enemy_health_pct=enemy_health_pct,
            berserker_health_pct=berserker_health_pct,
            barrier_active=barrier_active,
            action_taken=action_taken,
            symbolic_state=symbolic_state,
            reward=reward,
            outcome=outcome,
        )
        self.records.append(record)

    def to_dict_list(self) -> List[Dict[str, Any]]:
        return [asdict(record) for record in self.records]


if __name__ == "__main__":
    logger = ReplayLogger()
    logger.log_turn(
        turn_index=0,
        enemy_distance=0.3,
        enemy_health_pct=0.75,
        berserker_health_pct=0.4,
        barrier_active=True,
        action_taken="OVERDRIVE_BREAKER",
        symbolic_state="OVERDRIVE",
        reward=12.5,
        outcome="engaged",
    )
    print(logger.to_dict_list())
